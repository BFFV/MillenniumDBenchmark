# MillenniumDB Benchmarking Tools
Benchmarking tools for the MillenniumDB graph database engine, based on gMark.

# Usage

The following steps should be executed from inside the ``imfd`` directory:

1) Run ``compile-all.sh`` to **compile all necessary objects** from gMark's benchmarking tool.
2) **Choose/Create/Modify** an ``XML`` file inside the `config` directory (the schema for the graph data to be generated).
3) Run ``generate.sh NAME`` where ``NAME`` is the filename (only the name, without the extension/path) of the **chosen XML config file** from the previous step (this generates the data & workload).

The next few steps should be executed from inside the ``imfd/scripts`` directory:

4) Run ``parse_data.py DATA OUT`` where ``DATA`` is the file containing the **generated graph RDF data** and ``OUT`` is the desired output file (this converts the data to the MillenniumDB format).
5) Run ``parse_sparql.py WORKLOAD OUT`` where ``WORKLOAD`` is the directory containing the generated **SPARQL** queries (with the ``.sparql`` extension) and ``OUT`` is the desired output directory (this converts the query workload to the MillenniumDB format).
* You can also run ``parse_cypher.py WORKLOAD OUT`` with the same parameters as in step 5 if the workload is in **openCypher** format (with the ``.cypher`` extension).
6) **Create a database from the generated data (step 4)** with the MillenniumDB engine.
7) **Manually start** the MillenniumDB **server** to prepare for the benchmarking process.
8) Finally, execute ``run_benchmark.py WORKLOAD OUT`` where ``WORKLOAD`` is the directory containing the **already processed** queries and ``OUT`` is the desired output directory to store the results and benchmark statistics.
