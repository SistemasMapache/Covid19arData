# extrae casos
with open('parte.txt') as infile, open('fallecidos.txt', 'w') as outfile:
    copy = False
    for line in infile:
        if line.strip().startswith('Se registraron'):
            copy = True
            outfile.write(str(line))
            continue
        elif line.strip().startswith("Del total de casos"):
            copy = False
            continue
        elif line.strip().startswith("A la fecha"):
            copy = False
            continue
        elif line.strip().startswith("Detalle por provincia"):
            copy = False
            continue
        elif copy:
            if str(line) != '':
                outfile.write(str(line))
