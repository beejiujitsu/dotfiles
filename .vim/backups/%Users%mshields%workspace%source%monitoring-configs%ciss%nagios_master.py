Vim�UnDo� �h�ަW�5���-P��;MP��T�����e�P   �   WRUNBOOK = Actions(runbook='https://confluence.twitter.biz/display/CISS/Naemon+Runbook')      U      "       "   "   "    X#�r    _�                            ����                                                                                                                                                                                                                                                                                                                                                             X#c_     �         �      from mon import cql, util5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X#c_     �         �      from mon import cql, utiol5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                             X#ca     �   
      �       �   
      �    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X#cl     �         �       �         �    5�_�                       
    ����                                                                                                                                                                                                                                                                                                                                                             X#cp     �         �       �         �    5�_�                       6    ����                                                                                                                                                                                                                                                                                                                                                             X#c�    �         �      6RUNBOOK = Actions(runbook='https://confluence.twitter.5�_�                       4    ����                                                                                                                                                                                                                                                                                                                                                             X#c�     �         �      9from mon.core import Dashboard, Section, SimpleInstrument5�_�      	                 4    ����                                                                                                                                                                                                                                                                                                                                                             X#c�     �         �      9from mon.core import Dashboard, Section, SimpleInstrument5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             X#c�    �         �      9from mon.core import Dashboard, Section, SimpleInstrument5�_�   	              
   L       ����                                                                                                                                                                                                                                                                                                                                                             X#c�    �   K   M   �      %def DASHBOARD(naemon=None, **kwargs):5�_�   
                 S   @    ����                                                                                                                                                                                                                                                                                                                                                             X#c�     �   N   P           �   R   U   �      A    sections=[naemon_master.make_section(**naemon), INSTRUMENTS])5�_�                    Q       ����                                                                                                                                                                                                                                                                                                                                                             X#c�     �   N   P          �=`=jedi=0, =`=                    (sections=[], key_indicators=HOST_HEALTH_INSTRUMENTS, notifications=DEFAULT_NOTIFICATION_GROUPS, team="ciss-team", name="{{id}}", *_***kwargs*_*) =`=jedi=`=5�_�                    Q       ����                                                                                                                                                                                                                                                                                                                                                             X#c�     �   N   P          �=`=jedi=0, =`=                    (*_*sections=[]*_*, key_indicators=HOST_HEALTH_INSTRUMENTS, notifications=DEFAULT_NOTIFICATION_GROUPS, team="ciss-team", name="{{id}}", **kwargs) =`=jedi=`=5�_�                    Q       ����                                                                                                                                                                                                                                                                                                                                                             X#c�     �   P   T   �          id='{{target}}',   /    name='Nagios master {{suffix}} ({{zone}})',   @    sections=[naemon_master.make_section(**naemon), INSTRUMENTS]5�_�                    Q       ����                                                                                                                                                                                                                                                                                                                                                             X#c�     �   P   T   �        id='{{target}}',   -  name='Nagios master {{suffix}} ({{zone}})',   >  sections=[naemon_master.make_section(**naemon), INSTRUMENTS]5�_�                    Q       ����                                                                                                                                                                                                                                                                                                                                                             X#c�    �   P   T   �          id='{{target}}',   /    name='Nagios master {{suffix}} ({{zone}})',   @    sections=[naemon_master.make_section(**naemon), INSTRUMENTS]5�_�                    j       ����                                                                                                                                                    j                                                                                                                                                                                                       X#c�    �   i   n   �      (    # CISS-3252, atlc is the live master   )    # List[Pair(Profile, Boolean live?))]   C    (PROD_PROFILE(zone='smfc', role='nagios.prod.master'), False,),   A    (PROD_PROFILE(zone='atlc', role='nagios.prod.master'), True,)5�_�                    q       ����                                                                                                                                                    j                                                                                                                                                                                                       X#c�    �   p   r   �      `    DASHBOARD(naemon={'active_master': livep}).bind(profile) for profile, livep in prod_profiles5�_�                    q       ����                                                                                                                                                    j                                                                                                                                                                                                       X#c�    �   p   r   �      b      DASHBOARD(naemon={'active_master': livep}).bind(profile) for profile, livep in prod_profiles5�_�                    ~       ����                                                                                                                                                    j                                                                                                                                                                                                       X#c�    �   {   }           �   }      �      I      DASHBOARD(naemon={'active_master': False}), parsed_staging_profiles5�_�                    �        ����                                                                                                                                                    �                                                                                                                                                                                                       X#c�   	 �   �   �          if __name__ == '__main__':   #  RESULTS = dashboards(audubondata)     DUMP = util.dumps(RESULTS)     print(DUMP)5�_�                    L       ����                                                                                                                                                                                                                                                                                                                                                            X#c�   
 �   K   M   �      %def dashboard(naemon=None, **kwargs):5�_�                    q        ����                                                                                                                                                                                                                                                                                                                                                            X#c�    �   p   r          b      dashboard(naemon={'active_master': livep}).bind(profile) for profile, livep in prod_profiles5�_�                    q   F    ����                                                                                                                                                                                                                                                                                                                                                            X#c�    �   p   s   �      i      naemon_dashboard(naemon={'active_master': livep}).bind(profile) for profile, livep in prod_profiles5�_�                           ����                                                                                                                                                                                                                                                                                                                                                            X#d    �   |   ~           �   ~   �   �      I      dashboard(naemon={'active_master': False}), parsed_staging_profiles5�_�                    L   ,    ����                                                                                                                                                                                                                                                                                                                                                            X#d    �   K   M   �      ,def naemon_dashboard(naemon=None, **kwargs):5�_�                    L   Q    ����                                                                                                                                                                                                                                                                                                                                                            X#d!    �   K   M   �      Qdef naemon_dashboard(naemon=None, **kwargs):  # pylint: disable=missing-docstring5�_�                       $    ����                                                                                                                                                                                                                                                                                                                                                            X#d+    �         �      $def simple_ts(keyspace, instrument):5�_�                            ����                                                                                                                                                                                                                                                                                                                                                            X#d8     �                2def simple_instrument(name, keyspace, instrument):5�_�                            ����                                                                                                                                                                                                                                                                                                                                                            X#d>    �                0def rate_instrument(name, keyspace, instrument):5�_�                     #        ����                                                                                                                                                                                                                                                                                                                                                            X#dB    �   "   $          %def vex_instrument(name, instrument):5�_�      !               '        ����                                                                                                                                                                                                                                                                                                                                                            X#dF     �   &   (          .def notification_instrument(name, instrument):5�_�       "           !   +        ����                                                                                                                                                                                                                                                                                                                                                            X#dK    �   *   ,          (def notification_rate(name, instrument):5�_�   !               "      U    ����                                                                                                                                                                                                                                                                                                                                                             X#�q    �         �      WRUNBOOK = Actions(runbook='https://confluence.twitter.biz/display/CISS/Naemon+Runbook')5��