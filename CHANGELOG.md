# CHANGELOG

* v1.1.1d [2021-01-08]: Fixed Switch.can_discard for Q, A to always be discardable 
  Fixed test_can_discard__allows_queen from K to Q
  Fixed user_interface.get_player_information to randomise AI type


* v1.1.1c [2021-01-08]: Fixed player not switching to the other
  Fixed initial game flags for setup_round
  Fixed user_interface.select_player type error issue
  Fixed Switch.draw4 not being set to True when Q is discarded
  

* v1.1.1b [2021-01-06]: Fixed bugs related to starting a game
  Fixed players/bots instantiation when switch.py is ran
  Fixed index for cards at UI.select_card


* v1.1.1a [2021-01-06]: Fixed bugs that won't allow game to run.
  Fixed SimpleAI.ask_for_swap.
  Fixed missing () for run_game for running switch.py.
  

* v1.1.0 [2019-11-08]: Added a SmartAI computer opponent.
  Added strategy players.SmartAI
  None of the bugs have been fixed.
  

* v1.1.0 [2019-10-25]: First major release.
  This version is known to contain some bugs.
