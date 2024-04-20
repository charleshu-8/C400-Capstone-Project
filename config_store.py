#==================================
# Store globlly used information here
#==================================

# List of files we want to process into single CSV data set
files = ["github.csv", "google.csv", "reuters.csv", "wikipedia.csv", "youtube.csv"]

# List of features we want to extract per file
features = ["Length", "Protocol", "Info"]

# Mapping of string values to integers to simplify output prediction for predictive models
siteMappings = {
    "github.csv": 0,
    "google.csv": 1,
    "reuters.csv": 2,
    "wikipedia.csv": 3,
    "youtube.csv": 4,
}
protocolMappings = {
    "TLSv1.3": 0,
    "TCP": 1,
}
infoMappings = {
    "[PSH, ACK]": 0,
    "[SYN, ACK]": 1,
    "[FIN, ACK]": 2,
    "[FIN]": 3,
    "[SYN]": 4,
    "[PSH]": 5,
    "[ACK]": 6,
    "[RST]": 7,
    "Server Hello, Change Cipher Spec, Application Data": 8,
    "Change Cipher Spec, Application Data": 9,
    "Application Data, Application Data, Application Data": 10,
    "Application Data, Application Data": 11,
    "Client Hello": 12,
    "Server Hello": 13,
    "Change Cipher Spec": 14,
    "Application Data": 15,
    "Continuation Data": 16,
}

# Directory for data set used for all models
targetDataSet = "sanitized_data/sanitized_data_2024-04-19_07-41-40-490885_mapped.csv"

# Randomizer seed
randomSeed = 201

# k-fold value
k = 10
