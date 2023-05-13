from io import BytesIO
from typing import Annotated, Optional, Any
from pure_protobuf.annotations import Field, uint, int32, int64
from pure_protobuf.message import BaseMessage
from pydantic import BaseModel, validator, root_validator


from pyutils import JSONExportable


class BattleResultsDat():
	arena_ubuffer:uint
	buffer : bytes


class AvatarInfo(BaseMessage, JSONExportable):
	# #[prost(string, tag = "2")]
	# pub gfx_url: String,
	gfx_url: Annotated[str, Field(2)]

	# #[prost(string, tag = "3")]
	# pub gfx2_url: String,
	gfx2_url: Annotated[str, Field(3)]

	# #[prost(string, tag = "4")]
	# pub kind: String,
	kind: Annotated[str, Field(4)]


class Avatar(BaseMessage, JSONExportable):
	# #[prost(message, required, tag = "2")]
	# pub info: AvatarInfo,
	info : Annotated[AvatarInfo, Field(2)]


class Protagonist(BaseMessage, JSONExportable):
	# Field root:8
	
	# The field is negative (-2) if the player is auto-destroyed by inactivity
	hitpoints_left	 	: Annotated[int, Field(1)] = 0
	# credits are base in PlayerResultsInfo, total in Protagonist
	credits_total 		: Annotated[int, Field(2)] = 0
	exp_total 			: Annotated[int, Field(3)] = 0
	shots_made 			: Annotated[uint, Field(4)] = uint(0)
	shots_hit 			: Annotated[uint, Field(5)] = uint(0)
	shots_splash 		: Annotated[uint, Field(6)] = uint(0)
	shots_pen 			: Annotated[uint, Field(7)] = uint(0)
	damage_made 		: Annotated[uint, Field(8)] = uint(0)
	damage_assisted 	: Annotated[uint, Field(9)] = uint(0)
	damage_assisted_track: Annotated[uint, Field(10)] = uint(0)
	damage_received 	: Annotated[uint, Field(11)] = uint(0)
	hits_received 		: Annotated[uint, Field(12)] = uint(0)
	hits_bounced 		: Annotated[uint, Field(13)] = uint(0)
	hits_splash 		: Annotated[uint, Field(14)] = uint(0)	
	hits_pen 			: Annotated[uint, Field(15)] = uint(0)
	enemies_spotted 	: Annotated[uint, Field(16)] = uint(0)
	enemies_damaged 	: Annotated[uint, Field(17)] = uint(0)
	enemies_destroyed 	: Annotated[uint, Field(18)] = uint(0)

	distance_travelled 	: Annotated[uint, Field(23)] = uint(0)
	time_alive			: Annotated[uint, Field(24)] = uint(0)

	killed_by_res_id	: Annotated[Optional[uint], Field(25)] = None
	# 26 <chunk> = bytes (4)
	#         0000   C6 03 D3 03

	exp_for_damage		: Annotated[uint, Field(29)] = uint(0)
	exp_for_assist		: Annotated[uint, Field(30)] = uint(0)
	exp_team_bonus		: Annotated[uint, Field(31)] = uint(0)
	wp_points_earned	: Annotated[uint, Field(32)] = uint(0)
	wp_points_stolen	: Annotated[uint, Field(33)] = uint(0)
	# 36 <varint> = 129

	account_id 			: Annotated[uint, Field(101)]
	team 				: Annotated[uint, Field(102)]
	tank_id 			: Annotated[uint, Field(103)]
	
	# 105 <varint> = -1 (18446744073709551615)
	# 106 <varint> = 5112

	damage_blocked 	: Annotated[uint, Field(117)] = uint(0)
	# 119 <varint> = 1


class PlayerInfo(BaseMessage, JSONExportable):
	# Field = root:201
	nickname: Annotated[str, Field(1)]
	# platoon ID OR an id for a tournament team (both sides the same)
	platoon_id 		: Annotated[Optional[uint], Field(2)] = None
	team 			: Annotated[uint, Field(3)]

	# Field 4: unknown , varint

	clan_tag: Annotated[Optional[str], Field(5)] = None

	# #[prost(message, required, tag = "7")]
	# pub avatar: Avatar,
	avatar : Annotated[Avatar, Field(7)]


class Player(BaseMessage, JSONExportable):
	#   /// Player's account ID.
	# #[prost(uint32, tag = "1")]
	# pub account_id: u32,
	account_id : Annotated[uint, Field(1)]

	# /// Player's extended information.
	# #[prost(message, required, tag = "2")]
	# pub info: PlayerInfo,
	info : Annotated[PlayerInfo, Field(2)]


class PlayerResultsInfo(BaseMessage, JSONExportable):
	# Field = root:301
	credits_base 		: Annotated[uint, Field(2)] = uint(0)
	exp_base 			: Annotated[uint, Field(3)] = uint(0)
	shots_made 			: Annotated[uint, Field(4)] = uint(0)
	shots_hit 			: Annotated[uint, Field(5)] = uint(0)
	shots_splash 		: Annotated[uint, Field(6)] = uint(0)
	shots_pen 			: Annotated[uint, Field(7)] = uint(0)
	damage_made 		: Annotated[uint, Field(8)] = uint(0)
	damage_assisted 	: Annotated[uint, Field(9)] = uint(0)
	damage_assisted_track : Annotated[uint, Field(10)] = uint(0)
	damage_received 	: Annotated[uint, Field(11)] = uint(0)
	hits_received 		: Annotated[uint, Field(12)] = uint(0)
	hits_bounced 		: Annotated[uint, Field(13)] = uint(0)
	hits_splash 		: Annotated[uint, Field(14)] = uint(0)	
	hits_pen 			: Annotated[uint, Field(15)] = uint(0)
	enemies_spotted 	: Annotated[uint, Field(16)] = uint(0)
	enemies_damaged 	: Annotated[uint, Field(17)] = uint(0)
	enemies_destroyed 	: Annotated[uint, Field(18)] = uint(0)

	distance_travelled 	: Annotated[uint, Field(23)] = uint(0)
	time_alive			: Annotated[uint, Field(24)] = uint(0)

	SOME_id 			: Annotated[uint, Field(25)] = uint(0)   # field root:302

	exp_for_damage		: Annotated[uint, Field(29)] = uint(0)
	exp_for_assist		: Annotated[uint, Field(30)] = uint(0)
	exp_team_bonus		: Annotated[uint, Field(31)] = uint(0)
	wp_points_earned	: Annotated[uint, Field(32)] = uint(0)
	wp_points_stolen	: Annotated[uint, Field(33)] = uint(0)

	account_id 			: Annotated[uint, Field(101)]
	team 				: Annotated[uint, Field(102)]
	tank_id 			: Annotated[uint, Field(103)]

	# /// Rating for the Rating Battles.
	# ///
	# /// Note, that this is **not** the game client's displayed rating.
	# /// This field matches the `mm_rating` as returned by the Wargaming.net API.
	# ///
	# /// The display rating is calculated as: `3000.0 + mm_rating * 10.0`.
	# #[prost(float, optional, tag = "107")]
	# pub mm_rating: Option<f32>,

	# #[prost(uint32, tag = "117")]
	# pub damage_blocked: u32,
	damage_blocked 	: Annotated[uint, Field(117)] = uint(0)


class PlayerResults(BaseMessage, JSONExportable):
	# /// Looks like some sort of sequential result ID. They reference each other,
	# /// but I haven't figured this out yet.
	# #[prost(uint32, tag = "1")]
	# pub result_id: u32,
	result_id : Annotated[uint, Field(1)]

	# /// Extended player's results information.
	# #[prost(message, required, tag = "2")]
	# pub info: PlayerResultsInfo,
	info : Annotated[PlayerResultsInfo, Field(2)]


class BattleResults(BaseMessage, JSONExportable):
	
	map_id 		: Annotated[int, Field(1)]
	battle_mode : int = 0
	battle_start_timestamp : Annotated[int64, Field(2)]

	# #[prost(enumeration = "TeamNumber", optional, tag = "3")]
	# pub winner_team_number: Option<i32>,
	winner_team : Annotated[Optional[int], Field(3)] = None

	# Field 4: spawn(NO)
	# xxx : Annotated[uint, Field(4)] = uint(1)

	# Field 5: unknown
	# xxx : Annotated[uint, Field(4)] = uint(1)

	protagonist: Annotated[Protagonist, Field(8)]

	# This is also shown in 'meta.json' file's 'arenaBonusType' field
	room_type : Annotated[uint, Field(9)] = uint(0)

	free_xp 	: Annotated[uint, Field(137)] = uint(0)
	base_xp 	: Annotated[uint, Field(181)] = uint(0)
	credits_base : Annotated[uint, Field(183)] = uint(0)

	players 		: Annotated[list[Player], Field(201)] = list()
	players_results : Annotated[list[PlayerResults], Field(301)] = list()


	@root_validator(pre=False)
	def read_map_id(cls, values: dict[str, Any]) -> dict[str, Any]:
		# map_id (Field=1) has sometimes a flag 0x1 set
		# i.e. Field = map_id | (0x1 << 16 )
		map_id : int = int(values['map_id'])
		values['map_id'] 	  = map_id  & 0xffff  # First 2 bytes
		values['battle_mode'] = map_id >> 16      # second 2 bytes 
		return values