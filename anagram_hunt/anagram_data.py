"""Anagram Hunt Data Module"""
# Dictionary mapping word lengths to valid anagram sets
anagrams = {
    5: [
        ["abets", "baste", "betas", "beast", "beats"],
        ["acres", "cares", "races", "scare"],
        ["alert", "alter", "later"],
        ["angel", "angle", "glean"],
        ["baker", "brake", "break"],
        ["bared", "beard", "bread", "debar"],
        ["dater", "rated", "trade", "tread"],
        ["below", "bowel", "elbow"],
        ["caret", "cater", "crate", "trace", "react"]
    ],
    6: [
        ["arrest", "rarest", "raster", "raters", "starer"],
        ["carets", "caters", "caster", "crates", "reacts", "recast", "traces"],
        ["canter", "nectar", "recant", "trance"],
        ["danger", "gander", "garden", "ranged"],
        ["daters", "trades", "treads", "stared"]
    ],
    7: [
        ["allergy", "gallery", "largely", "regally"],
        ["aspired", "despair", "diapers", "praised"],
        ["claimed", "decimal", "declaim", "medical"],
        ["dearths", "hardest", "hatreds", "threads", "trashed"],
        ["detains", "instead", "sainted", "stained"]
    ],
    8: [
        ["parroted", "predator", "prorated", "teardrop"],
        ["repaints", "painters", "pantries", "pertains"],
        ["restrain", "retrains", "strainer", "terrains", "trainers"],
        ["construe", "counters", "recounts", "trounces"]
    ]
}
