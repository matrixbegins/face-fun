import boto3
from rekognition_image import RekognitionImage
from constants import quote_dict


class FaceHandler:
    """
        Represents one face detection call and the response of it.
        Raises botocore.exceptions.ClientError if API call to Rekognition fails.
    """

    def __init__(self, payload, img_name):
        rekognition_client = boto3.client('rekognition')
        self.rekog_obj = RekognitionImage(
            {'Bytes': payload}, img_name, rekognition_client)


        print("Analyzing face............")
        self.face_meta_data = self.rekog_obj.detect_faces()
        print(f"Found {len(self.face_meta_data)} faces")
        # for face in self.face_meta_data:
        #     print("face data:: ", face.to_dict())

        if len(self.face_meta_data) < 1:
            raise FileNotFoundError("No faces present in the given Image.")


    def extract_face_attributes(self):
        first_face = self.face_meta_data[0]


    def get_face_quotes(self):
        face_attrs = extract_face_attributes()

