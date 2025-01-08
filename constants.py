
import os

exclude_profiles_by_project = {
    "Bera_faucet": ["Ali Odonnell"],
    "Mint": ["Anton Andreev"],
}

profiles = {
    "0": {
        "name": "main",
        "order": "1",
        "address": {
            "eth": "0x95d1ba73fd9d3b3a2ff491b312d5eb9f462a649a"
        },
        "projects": {
            "Kong": {
                "delay_click": 0.07,
            }
        },
    },
    "166631615": {
        "name": "Anton Andreev",
        "order": "2", 
        "address": {
            "eth": "0xe87f901f7159FFf231D05441CBD367Ab6FC7Daa1"
        },
    },
    "166631158": {
        "name": "Carla Trujillo",
        "order": "3",
        "address": {
            "eth": "0x0C1DdA3aFd38f4D69770fA0aa5213032E8d6350b"
        },
    },
    "166630433": {
        "name": "Manpreet Singh",
        "order": "4",
        "address": {
            "eth": "0x8B0F73E2a2b4a06D01300057496bb5B8017A0f2c"
        },
    },
    "166629784": {
        "name": "Kristina Benton",
        "order": "5",
        "address": {
            "eth": "0xC62cCbFe06e1efb42fE43Db4c5ADC7Def613b534"
        },
    },
    "166629057": {
        "name": "Fuat Rashidov",
        "order": "6",
        "address": {
            "eth": "0x195A7835d04FB08C2992BBd3a26E4D81218A7D0C"
        },
    },
    "166516682": {
        "name": "Шамиль Камалитдинов",
        "order": "7",
        "address": {
            "eth": "0xDda0Aee84eAf8d6fa124ed86b7c79177C940548D"
        },
    },
    "166515137": {
        "name": "Ali Odonnell",
        "order": "8",
        "address": {
            "eth": "0xF70594ce98F5c176BBE05775613a9a1fB5178648"
        },
    },
    "166514316": {
        "name": "Далер Рахмет-Заде",
        "order": "9",
        "address": {
            "eth": "0x084cB8aC7E5cf922704B4F4cA4ADFA69a63E8423"
        },
    },
    "166511830": {
        "name": "Sergey Anisimov",
        "order": "10",
        "address": {
            "eth": "0xb10781675E0699d5082fA39FE71802112B19F4A0"
        },
    },
}

script_dir = os.path.dirname(os.path.abspath(__file__))