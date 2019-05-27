from mongoengine import Document, connect, StringField, IntField, ListField
import Util

db_db = "sjtu"
db_host = "localhost"
connect(db=db_db, host=db_host)

class Server(Document):
    domain = StringField(required=True)
    port = StringField(required=True)
    software = StringField(required=True)
    lic = StringField(required=True)


class Matlab(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class Solidworks(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class Altium(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class Mentors(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class Labview(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class Solidthinking(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()


class CurveFittingToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class Simulink(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class PolySpace_Bug_Finder_Engine(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class AerospaceBlockset(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class AerospaceToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class AntennaToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class AudioSystemToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class AutomatedDrivingToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class BioinformaticsToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class CommunicationToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class VideoandImageBlockset(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()


class ControlToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class SignalBlocks(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class DataAcqToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class DatabaseToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class DatafeedToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class NeuralNetworkToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class EconometricsToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class FilterDesignHDLCoder(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class FinInstrumentsToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class FinancialToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class FuzzyToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class GPUCoder(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()


class GADSToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class SimulinkHDLCoder(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class EDASimulatorLink(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class ImageAcquistionToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class ImageToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class InstrControlToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class LTEHDLToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class LTEToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class MATLABCoder(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class MATLABBuilderForJava(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class Compiler(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class MATLABReportGen(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class MAPToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class MPCToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class MBCToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class OPCToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class OptimizationToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class DistribComputingToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class PDEToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class PhasedArraySystemToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class PolySpaceServerCCPP(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class PowertrainBlockset(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class PredMaintenanceToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class RFBlockset(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()


class RFToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class RiskManagementToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class RoboticsSystemToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class RobustToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class SignalToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class SimBiology(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class SimEvents(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class SimDriveline(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class PowerSystemBlocks(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class SimHydraulics(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class SimMechanics(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class Simscape(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class VirtualRealityToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class SLVerificationValidation(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class SimulinkCodeInspector(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class RealTimeWorkshop(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class SimulinkControlDesign(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class SimulinkCoverage(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class SimulinkDesignOptim(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class SimulinkDesignVerifier(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class RealTimeWinTarget(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class SimulinkPLCCoder(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class XPCTarget(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class SIMULINKReportGen(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class SimulinkRequirements(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class SimulinkTest(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class ExecelLink(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class Stateflow(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class StatisticsToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class SymbolicToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class IdentificationToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class TextAnalyticsToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class TradingToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class VehicleDynamicsBlockset(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class VehicleNetworkToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class VisionHDLToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class WLANSystemToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class WaveletToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()

class SimElectronics(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()