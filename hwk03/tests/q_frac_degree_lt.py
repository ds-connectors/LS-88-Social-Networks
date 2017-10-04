test = {
  'name': 'Question',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> frac_degree_lt_neighbors(add_health_networks[3])
          0.70462633451957291
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> frac_degree_lt_neighbors(add_health_networks[30])
          0.68175765645805597
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
