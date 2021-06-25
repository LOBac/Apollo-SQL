# Descriptions for queries from queries.sql file
descriptions = [
    '''Select bateriums's ids of aerobic bacterias.''',
    '''Select the diseases and their symptoms that causes the bacterium 562''',
    '''Select bacterium's ids of bacteria whose genome cat. is "plasmid".''',
    '''Get bacterium's 625 genome length.''',
    '''Select all diseases that cause the coccus bacteria.''',
]

# Relation: [destination, origin(s), type]
# Types of relationships:
# 1 -> 1:1, 2 -> 1:N, 3 -> N:M
relations = [
    ['EMPLEADO', 'DEPARTAMENTO', 2],
    ['DEPARTAMENTO', 'EMPLEADO', 2],
    ['PRODUCTO', 'PROYECTO', 2],
    ['PROYECTO', 'DEPARTAMENTO', 2],
    ['EVENTO', 'EMPRESA_EXT', 2],
    ['UNIVERSIDAD', 'EMPRESA_EXT', 2],
    ['BECARIO', 'UNIVERSIDAD', 2],
    ['AFILIADO_A', ['DEPARTAMENTO', 'EMPRESA_EXT'], 3],
    ['PROVEE_A', ['PROYECTO', 'EMPRESA_EXT'], 3],
]
