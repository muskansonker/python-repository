import face_recognition # Library import kiya face recognition ke liye
import cv2 # Library import kiya image processing ke liye OpenCV se
import numpy as np # Library import kiya array operations ke liye numpy se
from sqlalchemy import create_engine, Column, Integer, String, Float # Library import kiya database ke liye sqlalchemy se
from sqlalchemy.ext.declarative import declarative_base # Library import kiya declarative_base ke liye sqlalchemy se
from sqlalchemy.orm import sessionmaker # Library import kiya sessionmaker ke liye sqlalchemy se

engine = create_engine('sqlite:///face_recognition.db') # Database se connect karne ke liye engine create kiya
Base = declarative_base() # declarative_base ka object create kiya

# Person class ko define kiya jo database table se map hoga
class Person(Base):
    _tablename_ = 'person' # Table ka name define kiya
    id = Column(Integer, primary_key=True) # Integer type ka column ID define kiya, jo primary key hai
    name = Column(String) # String type ka column Name define kiya
    encoding = Column(String) # String type ka column Encoding define kiya

    def _repr_(self):
        return f"<Person(name='{self.name}', encoding='{self.encoding}')>"

Base.metadata.create_all(engine) # Sabhi table ko database mein create karne ke liye Base class ka metadata create kiya
Session = sessionmaker(bind=engine) # Session create kiya aur database engine se bind kiya
session = Session() # Session create kiya

def add_person(name, encoding):
    new_person = Person(name=name, encoding=encoding) # Person class ka object create kiya aur parameters assign kiye
    session.add(new_person) # Session mein object ko add kiya
    session.commit() # Changes ko commit kiya

def get_all_persons():
    return session.query(Person).all() # Session se sabhi person ka data query kiya

def recognize_face():
    # Save kiye gaye face encodings ko database se load kiya
    persons = get_all_persons()
    known_face_encodings = [np.fromstring(person.encoding, sep=',') for person in persons]
    known_face_names = [person.name for person in persons]

    # Initialize variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    # Video capture device ko open kiya
    video_capture = cv2.VideoCapture(0)

    while True:
        # Single frame video capture kiya
        ret, frame = video_capture.read()

        # Faster face recognition processing ke liye frame ko 1/4 size mein resize kiya
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Image ko BGR color format se RGB color format mein convert kiya
        rgb_small_frame = small_frame[:, :, ::-1]

        # Har dusra frame ko process kiya jayega taki realtime performance acchi rahe
        if process_this_frame:
            # Current frame se sabhi faces ko detect kiya
            face_locations = face_recognition.face_locations(rgb_small_frame)
            # Current frame se sabhi faces ke encodings calculate kiye
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            # Current frame se sabhi faces ke names identify kiye
            face_names = []
            for face_encoding in face_encodings:
                # Kisi ek face encoding ko bhi sabhi saved encodings se match karein
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # Jis face ka encoding match karein, uska name assign karein
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Detect kiye gaye faces ke positions, encodings aur names ko video frame par display kiya
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Frame ko 1/4 size mein convert kiya keh ek baar mein jaldi display ho sakein
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Face ke rectangle border ko display kiya
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Face ke name ko display kiya
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Video frame display kiya
        cv2.imshow('Video', frame)

        # 'q' key press karne se video capture band ho jayega
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Video capture device aur window ko release kiya
    video_capture.release()
    cv2.destroyAllWindows()