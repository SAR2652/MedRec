import json
import sqlite3
#Field being fetched are in HL7 Format where:
#DG1 : Diagnosis ->
#EVN : Event-type
#GT1 : Guarantor
#IN1 : Insurance
#MSH : Messahe Header
#NK1 : Next of Kin/Associated parties
#NTE : Notes and Comments
#OBR : Observation request
#OBX : Observation Result
#ORC : Common Order
#PID : Patient ID -> Describes details of Patient
#FT1 : Financial Transactions (for DFT messages)
"""medi_string='''
{
    "DG1" : [

    ],
    "EVN" : [

    ],
    "GT1" : [

    ],
    "IN1" : [

    ],
    "MSH" : [

    ],
    "NK1" : [

    ],
    "NTE" : [

    ],
    "OBR" : [

    ],
    "OBX" : [

    ],
    "ORC" : [

    ],
    "PID" : [

    ],
    "FT1" : [

    ]
}
'''"""
"""data = json.loads(medi_string) #To convert json to python

new_string = json.dumps(data, indent=2) #To convert python to json"""
