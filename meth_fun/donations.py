donations = {
    'sara': 20,
    'saman': 40,
    'reza': 80,
    'seta': 160
}

def donations_analysis(don):
    person = ''
    total = 0 
    count = 0
    max_donation = -1

    for name, value in don.items():
        total += value
        count += 1
        if value > max_donation:
            person = name
            max_donation = value

    avg = total / count
    return total, avg, person

total, avg, max_person = donations_analysis(donations)
print(f"this is total of donations = {total}")
print(f"this is average of donations = {avg}")
print(f"this is the highest donation (special thanks to {max_person})")