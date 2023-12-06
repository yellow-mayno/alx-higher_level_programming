#!/usr/bin/python3
""" thyfdgh dgfdh fdgh dfghfdg """


def append_after(filename="", search_string="", new_string=""):
    """ F dfghdfgh dfgh dgf dfggfhdfg

    Args:
        filename: sfdgsfgdsfgsdfg
        search_string: dfgsdfg
        new_string: sfdgdsgfdsfgsfdg

    """

    sum = []
    with open(filename, 'r', encoding="utf-8") as rf:
        for lines in rf:
            sum += [lines]
            if search_string in lines:
                sum += [new_string]
    with open(filename, 'w', encoding="utf-8") as wf:
        wf.write("".join(sum))
