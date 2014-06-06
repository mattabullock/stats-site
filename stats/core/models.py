from django.db import models

# Create your models here.
class Player(models.Model):

	player_id = models.AutoField(primary_key=True)

	last_name = models.CharField(max_length=30)
	first_name = models.CharField(max_length=30)
	
	given_name = models.CharField(max_length=60)

	weight = models.IntegerField(max_value=3000)
	height = models.IntegerField(max_value=300)

	bats = models.CharField(max_length=3)
	throws = models.CharField(max_length=3)
	debut_game = models.DateField(null=True)
	final_game = models.DateField(null=True)

	mlb_id = models.CharField(max_length=12)
	retro_id = models.CharField(max_length=12)
	bbref_id = models.CharField(max_length=12)
	lahman_id = models.CharField(max_length=12)

	birth_year = models.IntegerField(max_value=9999)
	birth_month = models.IntegerField(max_value=12)
	birth_day = models.IntegerField(max_value=31)
	birth_country = models.CharField(max_length=30)
	birth_state = models.CharField(max_length=30)
	birth_city = models.CharField(max_length=30)

	death_year = models.IntegerField(max_value=9999, null=True)
	death_month = models.IntegerField(max_value=12, null=True)
	death_day = models.IntegerField(max_value=31, null=True)
	death_country = models.CharField(max_length=30, null=True)
	death_state = models.CharField(max_length=30, null=True)
	death_city = models.CharField(max_length=30, null=True)


class BatterSeason(models.Model):
	batter_season_id = models.AutoField(primary_key=True)
	player_id = models.ForeignKey(Player)
	season = models.IntegerField()
	team = models.CharField(max_length=30, null=True)
	games = models.IntegerField()
	plate_appearances = models.IntegerField()
	at_bats = models.IntegerField()
	runs = models.IntegerField()
	hits = models.IntegerField()
	doubles = models.IntegerField()
	triples = models.IntegerField()
	home_runs = models.IntegerField()

	def _get_singles(self):
    	return '%d - %d - %d - %d' % (self.hits, self.double, self.triple, self.home_runs)
	singles = property(_get_singles)
	
	rbis = models.IntegerField()
	stolen_bases = models.IntegerField()
	# stolen_bases_2 = models.IntegerField()
	# stolen_bases_3 = models.IntegerField()
	# stolen_bases_4 = models.IntegerField()
	caught_stealing = models.IntegerField()
	# caught_stealing_2 = models.IntegerField()
	# caught_stealing_3 = models.IntegerField()
	# caught_stealing_4 = models.IntegerField()
	# pickoffs = models.IntegerField()
	# caught_stealing_pickoffs = models.IntegerField()
	# oob = models.IntegerField()
	# oob1 = models.IntegerField()
	# oob2 = models.IntegerField()
	# oob3 = models.IntegerField()
	# oob4 = models.IntegerField()
	# first_single = models.IntegerField()
	# first_single_second = models.IntegerField()
	# first_single_third_home = models.IntegerField()
	# first_double = models.IntegerField()
	# first_double_third = models.IntegerField()
	# first_double_home = models.IntegerField()
	# second_single = models.IntegerField()
	# second_single_third = models.IntegerField()
	# second_single_home = models.IntegerField()
	# bases_taken = models.IntegerField()
	walks = models.IntegerField()
	strike_outs = models.IntegerField()
	battingavg = models.DecimalField(max_digits=4, decimal_places=3)
	obp = models.DecimalField(max_digits=4, decimal_places=3)

	def _get_slg(self):
		return '(%d + 2*%d + 3*%d + 4*%d)/%d' % (self.singles, self.doubles, self.triples, self.home_runs, self.at_bats)
    slg = property(_get_slg)
	
	def _get_ops(self):
    	return '%d + %d' % (self.obp, self.slg)
	ops = property(_get_ops)
	# ops_plus = models.IntegerField()
	# total_bases = models.IntegerField()
	# gdp = models.IntegerField()
	# hbp = models.IntegerField()
	# sac_hits = models.IntegerField()
	# sac_flys = models.IntegerField()
	# ibb = models.IntegerField()
	# runs_batting = models.IntegerField()
	# runs_basing = models.IntegerField()
	# rdp = models.IntegerField()
	# runs_fielding = models.IntegerField()
	# rpos = models.IntegerField()
	# raa = models.IntegerField()
	# waa = models.DecimalField(max_digits=2, decimal_places=1)
	# rrep = models.IntegerField()
	# rar = models.IntegerField()
	# war = models.DecimalField(max_digits=2, decimal_places=1)
	# waawl = models.DecimalField(max_digits=4, decimal_places=3)
	# seasonwl = models.DecimalField(max_digits=4, decimal_places=3)
	# owar = models.DecimalField(max_digits=2, decimal_places=1)
	# dwar = models.DecimalField(max_digits=2, decimal_places=1)
	# orar = models.DecimalField(max_digits=2, decimal_places=1)
	salary = models.IntegerField()



# class Pitcher(models.Model):
# 	pitcherid = models.AutoField(primary_key=True)
# 	pitcher = models.ForeignKey(Player)
# 	season = models.IntegerField()
# 	era = models.DecimalField(max_digits=5, decimal_places=3)

# class AtBat(models.Model):
# 	atbatid = models.AutoField(primary_key=True)
# 	batter = models.ForeignKey(Batter)
# 	pitcher = models.ForeignKey(Pitcher)
# 	game = models.ForeignKey(Game)

# class Pitch(models.Model):
# 	pitchid = models.AutoField(primary_key=True)
# 	pitcher = models.ForeignKey(Pitcher)
# 	atbat = models.ForeignKey(AtBat)
# 	game = models.ForeignKey(Game)

# class Game(models.Model):
# 	gameid = models.AutoField(primary_key=True)
# 	home =  models.CharField(max_length=30)

