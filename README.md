# Python Foundation

A structured collection of Python fundamentals, data structures, functions, control
flow, data analysis notebooks, and small Streamlit examples.

## Repository layout

```text
.
├── apps/
│   └── streamlit/             # Interactive Streamlit demos
├── data/                      # Datasets used by notebooks
├── examples/
│   └── basics/                # Small, focused Python examples
│       ├── control_flow/
│       ├── data_structures/
│       ├── data_types_and_variables/
│       ├── functions/
│       ├── input_output/
│       └── operators/
├── notebooks/
│   ├── databases/             # SQLite examples
│   ├── data_science/          # NumPy, Pandas, Matplotlib, Seaborn
│   ├── foundations/           # Numbered Python learning sequence
│   └── math_and_statistics/   # Calculus, probability, statistics, algebra
├── .gitignore
├── requirements.txt
└── README.md
```

## Getting started

Create an environment and install the notebook and app dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Open notebooks from the `notebooks/` directory with Jupyter, or run a focused
example directly:

```bash
jupyter lab
python examples/basics/data_structures/lists.py
```

Run either Streamlit demo with:

```bash
streamlit run apps/streamlit/dataframe_demo.py
streamlit run apps/streamlit/widgets_demo.py
```

The recommended learning path is the numbered sequence in
`notebooks/foundations/`, followed by the focused examples in
`examples/basics/` and the applied notebooks.
 
