from mongoengine import *
import Util

db_db = "sjtu"
db_host = "localhost"
connect(db=db_db, host=db_host)

class Matlab(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class AudioSystemToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class BioinformaticsToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class VideoandImageBlockset(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class CurveFittingToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class NeuralNetworkToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class GadsToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class MapToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class OptimizationToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class RfToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class PowerSystemBlocks(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class SimulinkControlDesign(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class SymbolicToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class WaveletToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

if __name__=="__main__":
    testdata = Util.testdata()
    modules = testdata.keys()

    temp = data["MATLAB"]
    print(Matlab.objects.all())
    matlab = Matlab(date=Util.get_date(), time=Util.get_time(), total=temp["total"], use=temp["use"], metadata=temp["metadata"], user_data=temp["user_data"])
    matlab.save()
    print(Matlab.objects.all())