test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> add_health_clustering.num_rows == 84
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(np.corrcoef(add_health_clustering.column('num_nodes'), add_health_clustering.column('avg_clustering_coef'))[0,1], 2) == -.66
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