def main():
    with open("/home/vladaf/Документы/Python/References/static/input.txt", "r") as file:
        f = file.read()
        masF = f.split("\n")
    with open("/home/vladaf/Документы/Python/References/static/output.txt", "w") as file:
        file.write("\\begin{thebibliography}{99}\n")
        file.close()
    for i in masF:
        line = i.split('.')
        rbibitem = line[0]
        author = line[1].split(',')
        paper = line[2][1:]
        jour = line[3][1:]
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
                    if j!=author[-1]:
                        file.write(
                        ", "
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
                f"\\jour {jour}\n\t"
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