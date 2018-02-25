test = {
  'name': 'Question',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> str(round(frac_degree_lt_neighbors(add_health_networks[3]), 4))
          '0.7046'
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> str(round(frac_degree_lt_neighbors(add_health_networks[30]), 4))
          '0.6818'
          """,
          'hidden': False
        }                
      ],
            
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
