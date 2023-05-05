def update_records (dictionary_record,id,property,value):
    if id in record:
        if property != "tracks" and value != '':
            record[id][property] = value
        elif property == 'tracks' and record[id].get("tracks") is None and value != '':
            record[id]["tracks"] = list(value)
        elif property == 'tracks' and value != '':
            record[id]["tracks"].append(value)
        elif value == '':
            record[id].pop(property)
        return record
    

record_collection ={
    2548: {
    albumTitle: 'Slippery When Wet',
    artist: 'Bon Jovi',
    tracks: ['Let It Rock', 'You Give Love a Bad Name']
    },
    2468: {
    albumTitle: '1999',
    artist: 'Prince',
    tracks: ['1999', 'Little Red Corvette']
    },
    1245: {
    artist: 'Robert Palmer',
    tracks: []
    },
    5439: {
    albumTitle: 'ABBA Gold'
    }
}