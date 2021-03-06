import sys


# gMark to MillenniumDB RDF data
def parse_graph(in_graph, out_graph):
    out_file = open(out_graph, 'w')
    with open(in_graph, 'r') as file:
        for line in file:
            rdf = line.strip('\n').split(' ')
            parsed_line = f'Q{rdf[0]}->Q{rdf[2]} :p{rdf[1]}'
            out_file.write(parsed_line + '\n')
    out_file.close()


# Parse RDF graph data generated by gMark
if __name__ == '__main__':
    try:
        parse_graph(sys.argv[1], sys.argv[2])
    except IndexError:
        print('Args are missing!')
