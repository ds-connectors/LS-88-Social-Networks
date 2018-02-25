test = {
  'name': 'Question',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.round(np.mean(nbr_avg_degrees['avg_friends_degree']), 2)
          7.71
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> round(nbr_avg_degrees.where(nbr_avg_degrees['id'] == 6)['avg_friends_degree'][0], 2) == 5.4
          True
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
