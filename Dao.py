from mongoengine import Document, connect, StringField, IntField, ListField
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

class Simulink(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class PolySpace_Bug_Finder_Engine(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class AerospaceBlockset(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class AerospaceToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class AntennaToolbox(Document):
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

class AutomatedDrivingToolbox(Document):
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

class CommunicationToolbox(Document):
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


class ControlToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class SignalBlocks(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class DataAcqToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class DatabaseToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class DatafeedToolbox(Document):
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

class EconometricsToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class FilterDesignHDLCoder(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class FinInstrumentsToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class FinancialToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class FuzzyToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class GPUCoder(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)


class GADSToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class SimulinkHDLCoder(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class EDASimulatorLink(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class ImageAcquistionToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class ImageToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class InstrControlToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class LTEHDLToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class LTEToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class MATLABCoder(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class MATLABBuilderForJava(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class Compiler(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class MATLABReportGen(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class MAPToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class MPCToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class MBCToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class OPCToolbox(Document):
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

class DistribComputingToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class PDEToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class PhasedArraySystemToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class PolySpaceServerCCPP(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class PowertrainBlockset(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class PredMaintenanceToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class RFBlockset(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)


class RFToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class RiskManagementToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class RoboticsSystemToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class RobustToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class SignalToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class SimBiology(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class SimEvents(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class SimDriveline(Document):
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

class SimHydraulics(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class SimMechanics(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class Simscape(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class VirtualRealityToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class SLVerificationValidation(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class SimulinkCodeInspector(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class RealTimeWorkshop(Document):
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

class SimulinkCoverage(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class SimulinkDesignOptim(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class SimulinkDesignVerifier(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class RealTimeWinTarget(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class SimulinkPLCCoder(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class XPCTarget(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class SIMULINKReportGen(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class SimulinkRequirements(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class SimulinkTest(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class ExecelLink(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class Stateflow(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class StatisticsToolbox(Document):
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

class IdentificationToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class TextAnalyticsToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class TradingToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class VehicleDynamicsBlockset(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class VehicleNetworkToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class VisionHDLToolbox(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)

class WLANSystemToolbox(Document):
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

class SimElectronics(Document):
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField(required=True)
    user_data = ListField(required=True)