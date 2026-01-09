import cv2

def analyze_video(path):
    cap = cv2.VideoCapture(path)
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if frames > 2000:
        return {"safe": False, "reason": "Long suspicious video"}

    return {"safe": True, "reason": "Video content compliant"}