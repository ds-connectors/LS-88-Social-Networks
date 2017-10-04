test = {
  'name': 'Question',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.mean(add_health_msmts['avg_degree'])
          7.231034672208172
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> np.mean(add_health_msmts['avg_neighbor_degree'])
          8.7959161086127811
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> np.mean(add_health_msmts['frac_lt_neighbors']) 
          0.68504134158396413
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> np.corrcoef(add_health_msmts['avg_degree'], add_health_msmts['avg_neighbor_degree'])[0,1] 
          0.98938951260142327
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> np.corrcoef(add_health_msmts['avg_neighbor_degree'], add_health_msmts['frac_lt_neighbors'])[0,1]
          0.030922800711871038
          """,
          'hidden': False
        },         
      ],
            
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
