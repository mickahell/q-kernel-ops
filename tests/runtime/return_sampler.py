"""Generate sampler return."""
from ast import literal_eval
from qiskit_ibm_runtime import SamplerResult


def get_sampler() -> SamplerResult:
    """Function to get a sample of SamplerResult object."""
    data = SamplerResult(
        quasi_dists=[
            literal_eval(
                "{'1011':0.00390625,'0001':0.005859375,'0010':0.017578125,'1001':0.0029296875,"
                "'1000':0.0068359375,'1100':0.173828125,'1010':0.0234375,'1111':0.19140625,"
                "'0011':0.001953125,'0111':0.0361328125,'0000':0.0419921875,'1101':0.271484375,"
                "'0110':0.0537109375,'0100':0.1689453125} "
            ),
            literal_eval(
                "{'1000':0.0009765625,'1001':0.0029296875,'0001':0.0078125,'1011':0.00390625,"
                "'0010':0.02734375,'1101':0.2890625,'1010':0.0166015625,'1111':0.1728515625,"
                "'0110':0.052734375,'0100':0.1611328125,'0011':0.001953125,'0000':0.0361328125,"
                "'0111':0.033203125,'1100':0.193359375}"
            ),
            literal_eval(
                "{'1011':0.0029296875,'1001':0.0009765625,'0010':0.025390625,'0001':0.0126953125,"
                "'1101':0.2548828125,'0101':0.001953125,'1100':0.205078125,'1010':0.0283203125,"
                "'1111':0.1865234375,'1000':0.0048828125,'0110':0.0390625,'0100':0.1640625,"
                "'0011':0.00390625,'0000':0.03515625,'0111':0.0341796875}"
            ),
            literal_eval(
                "{'1011':0.001953125,'1000':0.0029296875,'1001':0.00390625,'0001':0.015625,"
                "'0011':0.001953125,'0000':0.044921875,'0111':0.0400390625,'0010':0.029296875,"
                "'1101':0.2548828125,'0110':0.0556640625,'0100':0.150390625,'1111':0.1640625,"
                "'1010':0.0146484375,'1100':0.2197265625}"
            ),
            literal_eval(
                "{'1011':0.001953125,'1000':0.0029296875,'0001':0.01171875,'0010':0.0322265625,"
                "'1010':0.021484375,'1111':0.1865234375,'1101':0.28515625,'0011':0.0009765625,"
                "'0111':0.0322265625,'0000':0.03515625,'1100':0.1865234375,'0110':0.046875,"
                "'0100':0.15625}"
            ),
            literal_eval(
                "{'1001':0.001953125,'1011':0.00390625,'1000':0.00390625,'0001':0.009765625,"
                "'0011':0.0009765625,'0111':0.029296875,'0000':0.0361328125,'1101':0.26953125,"
                "'0010':0.029296875,'1100':0.2041015625,'1010':0.01953125,'1111':0.1552734375,"
                "'0110':0.0634765625,'0100':0.1728515625}"
            ),
        ],
        metadata=[
            literal_eval("{'header_metadata': None, 'shots': 1024}"),
            literal_eval("{'header_metadata': None, 'shots': 1024}"),
            literal_eval("{'header_metadata': None, 'shots': 1024}"),
            literal_eval("{'header_metadata': None, 'shots': 1024}"),
            literal_eval("{'header_metadata': None, 'shots': 1024}"),
            literal_eval("{'header_metadata': None, 'shots': 1024}"),
        ],
    )
    return data
