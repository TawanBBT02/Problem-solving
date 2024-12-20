def seach_countries_by_letter(country_data:dict[str,str],letter:str)->list[str]:
    result = []
    for i in country_data:
        if letter in country_data[i]:
            result.append(country_data[i])
    return result

country_data = {
    "+1":"United States",
    "+44":"United Kingdom",
    "+91":"India",
    "+81":"Japan",
    "+49":"Germany",
    "+86":"China"
}
letter = "U"

print(seach_countries_by_letter(country_data,letter))