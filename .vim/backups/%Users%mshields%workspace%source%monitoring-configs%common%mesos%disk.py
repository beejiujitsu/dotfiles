Vim�UnDo� "�����0�w��`�
2�?$��� �N+�,k)   n   )      query='''default(0, zone({{zones}},   6                          W���   
 _�                     
   A    ����                                                                                                                                                                                                                                                                                                                                                             W��6    �                 �   	      n      C    predicates=None, actions=Empty, group=Empty, agg='', **kwargs):5�_�                    0        ����                                                                                                                                                                                                                                                                                                                                                             W��t     �   /   2   o      !    'warn': '> 85 for 10 of 10m',   $    'critical': '> 95 for 10 of 10m'5�_�                    4       ����                                                                                                                                                    4                                                                                                                                                                                                       W��    �   3   <   o          name=name,       description=description,       query='''zone({{zones}},   W    100 * {{agg}}(ts(mesos.container, {{source}}, executor.resource_manager.disk_used))   \    / {{agg}}(ts(mesos.container, {{source}}, executor.resource_manager.disk_reserved)))''',       predicates=predicates,       actions=actions,       group=group5�_�                    A   9    ����                                                                                                                                                    4                                                                                                                                                                                                       W���    �   =   ?           �   @   C   o      ;    predicates=None, actions=Empty, group=Empty, **kwargs):5�_�                    f       ����                                                                                                                                                    4                                                                                                                                                                                                       W���     �   e   g   p      "    'warn': '> 200K for 10 of 10m'5�_�                    f       ����                                                                                                                                                    4                                                                                                                                                                                                       W���     �   d   f   p      .  predicates = predicates if predicates else {   'warn': '> 200K for 10 of 10m'�   e   g   p      $      'warn': '> 200K for 10 of 10m'5�_�                    f       ����                                                                                                                                                    4                                                                                                                                                                                                       W���     �   d   f   o      L  predicates = predicates if predicates else {'warn': '> 200K for 10 of 10m'   }�   e   g   o        }5�_�      	              g       ����                                                                                                                                                    g   	                                                                                                                                                                                                    W���    �   f   n   n          name=name,       description=description,       query='''zone({{zones}},   X    rate(ts(mesos.container, {{source}}, executor.resource_manager.disk_used)) / 60)''',       predicates=predicates,       actions=actions,       group=group5�_�      
           	          ����                                                                                                                                                    g   	                                                                                                                                                                                                    W���    �      	   n      def disk_usage_monitor(5�_�   	              
   6       ����                                                                                                                                                    g   	                                                                                                                                                                                                    W��C     �   5   7   n            query='''zone({{zones}},5�_�   
                 8   Z    ����                                                                                                                                                    g   	                                                                                                                                                                                                    W��G    �   7   9   n      ^      / {{agg}}(ts(mesos.container, {{source}}, executor.resource_manager.disk_reserved)))''',5�_�                    i       ����                                                                                                                                                    g   	                                                                                                                                                                                                    W��`     �   h   j   n            query='''zone({{zones}},5�_�                    j   V    ����                                                                                                                                                    g   	                                                                                                                                                                                                    W��d    �   i   k   n      Z      rate(ts(mesos.container, {{source}}, executor.resource_manager.disk_used)) / 60)''',5�_�                   6       ����                                                                                                                                                    g   	                                                                                                                                                                                                    W���   	 �   5   7   n      )      query='''default(0, zone({{zones}},5�_�                     6       ����                                                                                                                                                    g   	                                                                                                                                                                                                    W���   
 �   5   7   n      )      query='''default(1, zone({{zones}},5�_�                    i       ����                                                                                                                                                    g   	                                                                                                                                                                                                    W���     �   h   j   n      )      query='''default(1, zone({{zones}},5��