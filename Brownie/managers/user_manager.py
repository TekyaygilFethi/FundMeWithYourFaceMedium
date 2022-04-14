import os

import pandas as pd
from ...FaceRecognition.recognition import capture


def CheckUserRole():
    df = pd.read_csv(
        os.path.normpath(os.path.join(os.getcwd(), "../Data/Csv/Users.csv"))
    )

    id, name = capture()

    user_role = None

    if id is not None and name is not None:
        user_role = df[(df["User"] == name) & (df["Id"] == int(id))]["Role"]

    return (name, user_role)
