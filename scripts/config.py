"""IETF network/design principle definitions with keyword patterns for detection."""

PRINCIPLES = [
    {
        "id": "end_to_end",
        "name": "End-to-end principle",
        "description": "Intelligence should be at endpoints, not in the network. Functions can only be correctly implemented at the application layer.",
        "rfc_refs": ["RFC 1958", "RFC 3724"],
        "keywords": [
            r"end.to.end\s+principle",
            r"end.to.end\s+argument",
            r"e2e\s+principle",
            r"saltzer",
            r"intelligence.*end\s*point",
            r"dumb\s+network",
            r"smart\s+endpoint",
        ],
    },
    {
        "id": "robustness",
        "name": "Robustness principle / Postel's law",
        "description": "Be conservative in what you send, be liberal in what you accept.",
        "rfc_refs": ["RFC 761", "RFC 1122", "RFC 9413"],
        "keywords": [
            r"postel.s?\s+law",
            r"robustness\s+principle",
            r"conservative.*send.*liberal.*accept",
            r"strict.*send.*tolerant.*accept",
            r"liberal.*accept",
            r"tolerant.*receive",
        ],
    },
    {
        "id": "layering",
        "name": "Layering principle",
        "description": "Protocol design organized in layers with clear separation of concerns.",
        "rfc_refs": ["RFC 1122", "RFC 3439"],
        "keywords": [
            r"layer(?:ing)?\s+principle",
            r"layer\s+violation",
            r"cross.layer",
            r"protocol\s+layer(?:ing)?",
            r"osi\s+model",
            r"layer\s+(?:one|two|three|four|seven|1|2|3|4|7)\b",
        ],
    },
    {
        "id": "fate_sharing",
        "name": "Fate sharing",
        "description": "Related parts of a system fail together. State maintained only at endpoints.",
        "rfc_refs": ["RFC 1958"],
        "keywords": [
            r"fate.shar",
            r"fail\s+together",
            r"state.*endpoint",
        ],
    },
    {
        "id": "least_surprise",
        "name": "Principle of least surprise",
        "description": "System should behave in ways that least surprise users and implementers.",
        "rfc_refs": ["RFC 3439"],
        "keywords": [
            r"least\s+(?:surprise|astonishment)",
            r"principle\s+of\s+least",
            r"most\s+usable.*least.*astonish",
        ],
    },
    {
        "id": "rough_consensus",
        "name": "Rough consensus and running code",
        "description": "IETF decision-making: address all issues but not necessarily accommodate all. Prefer working implementations.",
        "rfc_refs": ["RFC 7282"],
        "keywords": [
            r"rough\s+consensus",
            r"running\s+code",
            r"humming",
            r"hum\s+(?:in|on|for|against)",
            r"we\s+reject.*kings.*presidents.*voting",
        ],
    },
    {
        "id": "ossification",
        "name": "Protocol ossification",
        "description": "Protocols becoming rigid due to middlebox interference. Use-it-or-lose-it for extension points.",
        "rfc_refs": ["RFC 9170"],
        "keywords": [
            r"ossif",
            r"grease",
            r"use.it.or.lose.it",
            r"middlebox.*interfere",
            r"protocol\s+agility",
        ],
    },
    {
        "id": "tussle",
        "name": "Tussle in cyberspace",
        "description": "Design for the inevitable tensions between stakeholders with different interests.",
        "rfc_refs": [],
        "keywords": [
            r"tussle",
            r"design\s+for\s+(?:choice|variation)",
            r"stakeholder.*conflict",
        ],
    },
    {
        "id": "simplicity",
        "name": "Simplicity / complexity management",
        "description": "Complexity is the primary impediment to scaling. Keep designs simple.",
        "rfc_refs": ["RFC 3439"],
        "keywords": [
            r"rfc\s*3439",
            r"complexity.*scal",
            r"keep\s+it\s+simple",
            r"simplicity\s+principle",
            r"unnecessary\s+complexity",
        ],
    },
    {
        "id": "trust",
        "name": "Trust as architectural principle",
        "description": "Trust relationships must be defined before protocol design.",
        "rfc_refs": ["RFC 3724"],
        "keywords": [
            r"trust\s+model",
            r"zero.trust",
            r"trust\s+anchor",
            r"trust\s+relationship",
            r"trust\s+boundar",
        ],
    },
    {
        "id": "connectivity",
        "name": "Connectivity as primary goal",
        "description": "The Internet's primary goal is universal connectivity.",
        "rfc_refs": ["RFC 1958"],
        "keywords": [
            r"universal\s+connectivity",
            r"global\s+reachability",
            r"connectivity.*primary",
            r"reachability.*goal",
        ],
    },
    {
        "id": "constant_change",
        "name": "Principle of constant change",
        "description": "The Internet must continue to evolve. Design for extensibility.",
        "rfc_refs": ["RFC 1958"],
        "keywords": [
            r"constant\s+change",
            r"evolvab",
            r"extensib",
            r"future.proof",
            r"backward.?compat",
        ],
    },
]

# Analysis metadata
ANALYSIS_TYPE = "ietf_principle_analysis"
ANALYSIS_VENDOR = "ietf-hackathon-125"
ANALYSIS_VERSION = "1.0"
CONTEXT_CHARS = 200  # characters of context around each match
