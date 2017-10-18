test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.mean(add_health_sp.column('num_nodes')) > 860
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(np.corrcoef(add_health_sp.column('avg_shortest_path'),add_health_sp.column('avg_degree'))[0,1],2)==-.65
          True
          """,
          'hidden': False,
          'locked': False
        }                
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}