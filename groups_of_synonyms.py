def find_group_of_synonyms():
    input_data = [{"Dg set": "Diesel generator"}, {"Organization": "Organisation"}, {"Group": "Organization"},
                  {"Orange": "Kinnu"}, {"Orange": "narangi"}]
    output = []

    for items in input_data:
        result = []
        for key, val in items.items():
            if not any(key in sublist for sublist in output) and not any(val in sublist for sublist in output):
                result.append(key)
                result.append(val)
                output.append(result)
            elif not any(key in sublist for sublist in output):
                for data in output:
                    if val in data:
                        data.append(key)
            elif not any(val in sublist for sublist in output):
                for data1 in output:
                    if key in data1:
                        data1.append(val)
    return output


response = find_group_of_synonyms()
print(response)
