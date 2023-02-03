def main():
    with open("/home/vladaf/Документы/Python/References/static/input.txt", "r") as file:
        f = file.read()
        masF = f.split("\n")
    with open("/home/vladaf/Документы/Python/References/static/output.txt", "w") as file:
        file.write("\\begin{thebibliography}{99}\n")
        file.close()
    for i in masF:
        line = i.replace(" //", ".").replace(". Vol. ", ";").replace(". Т. ", ";").replace(". P. ", ":").replace(". С. ", ":").replace("&", "and").replace("Ⅹ", "X").replace("Ⅰ", "I").replace("Ⅴ", "V").split(".")
        rbibitem = line[0]
        author = line[1].split(',')
        if line[3].find(";")>=0:                                    #книга
            book = line[2][1:].replace(";", ".")
            info = line[3][1:].replace(":", ".").replace(";", ".").split('.')
            publaddr = info[0]
            publ = info[1]
            year = info[2]
            other = line[4][1:].replace(",", ".").split('.')          
            total = other[0]
            totalpages = other[1][1:].replace(" p", "").replace(" с", "")
            with open("/home/vladaf/Документы/Python/References/static/output.txt", "a") as file:
                file.write(
                    f"\n\t\\RBibitem{{{rbibitem}}}\n\t"
                    f"\\by "
                )
                for j in author:
                    x = j[1:].split(" ")
                    fam = x[0]
                    if len(x[1])==2:
                        name = x[1][:1]
                        otch = x[1][1:]
                        file.write(
                            f"{name}.\,{otch}. ~{fam}"
                        )
                    else:
                        name = x[1]
                        file.write(
                            f"{name}.\ ~{fam}"
                        )
                    if j!=author[-1]:
                            file.write(
                            ", "
                        )
                file.write(
                    f"\n\t\\book {book}\n\t"
                    f"\\publaddr {publaddr}\n\t"
                    f"\\publ {publ}\n\t"
                    f"\\yr {year}\n\t"
                    f"\\totalpages {total}+{totalpages}\n\t"
                )
                if i.find("(")>=0:
                    left_id = i.find("(")+1
                    right_id = i.find(")")
                    serial_vol = i[left_id:right_id].split(';')
                    serial = serial_vol[0]
                    vol = serial_vol[1][8:]
                    file.write(
                        f"\\serial {serial}\n\t"
                        f"\\vol {vol}\n\t"
                    )
                if i.find("DOI:")>=0:
                    doi_id = i.find("DOI:")+5
                    doi = i[doi_id:-1]
                    file.write(
                        f"\crossref{{http://dx.doi.org/{doi}}}\n\t"
                    )
                file.close()
        elif line[3].find("В:")>=0 or line[3].find("In:")>=0:       #конференция
            paper = line[2][1:].replace(";", ".")
            inbook = line[3][1:].replace("В: ", "").replace("In: ", "").replace(":", ".")
            info = line[4][1:].replace(":", ".").replace(";", ".").split('.')
            publaddr = info[0]
            publ = info[1]
            year = info[2]
            other = line[5][1:].replace(",", ".").split('.')          
            vol = other[0]
            pages = other[1][1:].replace(" p", "").replace(" с", "")
            with open("/home/vladaf/Документы/Python/References/static/output.txt", "a") as file:
                file.write(
                    f"\n\t\\RBibitem{{{rbibitem}}}\n\t"
                    f"\\by "
                )
                for j in author:
                    x = j[1:].split(" ")
                    fam = x[0]
                    if len(x[1])==2:
                        name = x[1][:1]
                        otch = x[1][1:]
                        file.write(
                            f"{name}.\,{otch}. ~{fam}"
                        )
                    else:
                        name = x[1]
                        file.write(
                            f"{name}.\ ~{fam}"
                        )
                    if j!=author[-1]:
                            file.write(
                            ", "
                        )
                file.write(
                    f"\n\t\\paper {paper}\n\t"
                    f"\\inbook {inbook}\n\t"
                    f"\\publaddr {publaddr}\n\t"
                    f"\\publ {publ}\n\t"
                    f"\\yr {year}\n\t"
                    f"\\vol {vol}\n\t"
                    f"\\pages {pages}\n\t".replace("–", "--")
                )
                if i.find("DOI:")>=0:
                    doi_id = i.find("DOI:")+5
                    doi = i[doi_id:-1]
                    file.write(
                        f"\crossref{{http://dx.doi.org/{doi}}}\n\t"
                    )
                file.close()
        else:                                                       #статья
            paper = line[2][1:].replace(";", ".")
            jour = line[3][1:].replace(":", ".")
            other = line[4][1:].replace(":", ".").replace(";", ".").split('.')
            year = other[0]
            vol = other[1]
            pages = other[2].replace("–", "--")
            with open("/home/vladaf/Документы/Python/References/static/output.txt", "a") as file:
                file.write(
                    f"\n\t\\RBibitem{{{rbibitem}}}\n\t"
                    f"\\by "
                )
                for j in author:
                    x = j[1:].split(" ")
                    fam = x[0]
                    if len(x[1])==2:
                        name = x[1][:1]
                        otch = x[1][1:]
                        file.write(
                            f"{name}.\,{otch}. ~{fam}"
                        )
                    else:
                        name = x[1]
                        file.write(
                            f"{name}.\ ~{fam}"
                        )
                    if j!=author[-1]:
                            file.write(
                            ", "
                        )
                file.write(
                    f"\n\t\\paper {paper}\n\t"
                )
                if jour.find(":")>=0:
                    j = jour.split(":")
                    publaddr = j[0]
                    publ = j[1][1:]
                    file.write(
                        f"\\publaddr {publaddr}\n\t"
                        f"\\publ {publ}\n\t"
                    )
                else:
                    journal = jour.replace(";", ".")
                    file.write(
                        f"\\jour {journal}\n\t"
                    )
                file.write(
                    f"\\yr {year}\n\t"
                    f"\\vol {vol}\n\t"
                    f"\\pages {pages}\n\t"
                )
                if i.find("DOI:")>=0:
                    doi_id = i.find("DOI:")+5
                    doi = i[doi_id:-1]
                    file.write(
                        f"\crossref{{http://dx.doi.org/{doi}}}\n\t"
                    )
                file.close()
    with open("/home/vladaf/Документы/Python/References/static/output.txt", "a") as file:
        file.write("\n\\end{thebibliography}")
        file.close()
        
if __name__ == '__main__':
    main()