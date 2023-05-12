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
	# 1 <varint> = 784
	hitpoints_left : Annotated[uint, Field(1)]
	# 2 <varint> = 59759
	credits_total : Annotated[int, Field(2)] = 0
	# 3 <varint> = 3222
	exp_total : Annotated[int, Field(3)] = 0
	# 4 <varint> = 8
	shots_made : Annotated[uint, Field(4)] = uint(0)
	# 5 <varint> = 7
	shots_hit : Annotated[uint, Field(5)] = uint(0)
	# 6 <varint> = 6	
	shots_splash : Annotated[uint, Field(6)] = uint(0)
	# 7 <varint> = 6
	shots_pen : Annotated[uint, Field(7)] = uint(0)
	# 8 <varint> = 2165
	damage_dealt : Annotated[uint, Field(8)] = uint(0)
	# 9 <varint> = 1420	
	damage_assisted 	: Annotated[uint, Field(9)] = uint(0)

	damage_assisted_track : Annotated[uint, Field(10)] = uint(0)
	# 11 <varint> = 1124
	damage_received 	: Annotated[uint, Field(11)] = uint(0)

	# 12 <varint> = 5
	hits_received 		: Annotated[uint, Field(12)] = uint(0)
	# 13 <varint> = 2
	hits_bounced 		: Annotated[uint, Field(13)] = uint(0)
	
	hits_splash 		: Annotated[uint, Field(14)] = uint(0)	
	# 15 <varint> = 3
	hits_pen 			: Annotated[uint, Field(15)] = uint(0)
	
	# 17 <varint> = 3
	enemies_spotted 	: Annotated[uint, Field(16)] = uint(0)

	# 17 <varint> = 3
	enemies_damaged 	: Annotated[uint, Field(17)] = uint(0)
	
	# 18 <varint> = 2
	enemies_destroyed 	: Annotated[uint, Field(18)] = uint(0)
	
	# 23 <varint> = 667
	distance_travelled 	: Annotated[uint, Field(23)] = uint(0)
	# 24 <varint> = 172
	time_alive			: Annotated[uint, Field(24)] = uint(0)

	# 26 <chunk> = bytes (4)
	#         0000   C6 03 D3 03

	# 29 <varint> = 323
	exp_for_damage		: Annotated[uint, Field(29)] = uint(0)
	# 30 <varint> = 82
	exp_for_assist		: Annotated[uint, Field(30)] = uint(0)
	# 31 <varint> = 540
	exp_team_bonus		: Annotated[uint, Field(31)] = uint(0)
	
	# 32 <varint> = 80	
	# 33 <varint> = 80
	wp_points_earned		: Annotated[uint, Field(32)] = uint(0)
	wp_points_stolen		: Annotated[uint, Field(33)] = uint(0)
	# 36 <varint> = 129

	# 101 <varint> = 521458531
	account_id : Annotated[uint, Field(3)]
	# 102 <varint> = 2

	# 103 <varint> = 18001
	# 105 <varint> = -1 (18446744073709551615)
	# 106 <varint> = 5112
	# 117 <varint> = 350
	# 119 <varint> = 1


class PlayerInfo(BaseMessage, JSONExportable):
	# /// Player's nickname.
	# #[prost(string, tag = "1")]
	# pub nickname: String,
	nickname: Annotated[str, Field(1)]

	# platoon ID OR an id for a tournament team (both sides the same)
	platoon_id : Annotated[Optional[uint], Field(2)] = None

	# /// Player's team assignment.
	# #[prost(enumeration = "TeamNumber", tag = "3")]
	# pub team: i32,
	team : Annotated[uint, Field(3)]

	# #[prost(string, optional, tag = "5")]
	# pub clan_tag: Option<String>,
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
	# /// Credits earned – without special awards and medals and premium account excluded.
	# #[prost(uint32, tag = "2")]
	# pub credits_earned: u32,
	credits : Annotated[uint, Field(2)] = uint(0)

	# /// Base XP (the total without multipliers).
	# #[prost(uint32, tag = "3")]
	# pub base_xp: u32
	exp : Annotated[uint, Field(3)] = uint(0)

	# #[prost(uint32, tag = "4")]
	# pub n_shots: u32,
	n_shots : Annotated[uint, Field(4)] = uint(0)

	# #[prost(uint32, tag = "5")]
	# pub n_hits_dealt: u32,
	n_hits : Annotated[uint, Field(5)] = uint(0)


	# #[prost(uint32, tag = "7")]
	# pub n_penetrations_dealt: u32,
	n_pens : Annotated[uint, Field(7)] = uint(0)

	# #[prost(uint32, tag = "8")]
	# pub damage_dealt: u32,

	# /// TODO: distinguish the kinds of assisted damage.
	# #[prost(uint32, tag = "9")]
	# pub damage_assisted_1: u32,

	# /// TODO: distinguish the kinds of assisted damage.
	# #[prost(uint32, tag = "10")]
	# pub damage_assisted_2: u32,

	# #[prost(uint32, tag = "12")]
	# pub n_hits_received: u32,

	# #[prost(uint32, tag = "13")]
	# pub n_non_penetrating_hits_received: u32,

	# #[prost(uint32, tag = "15")]
	# pub n_penetrations_received: u32,

	# #[prost(uint32, tag = "17")]
	# pub n_enemies_damaged: u32,

	# #[prost(uint32, tag = "18")]
	# pub n_enemies_destroyed: u32,

	# #[prost(uint32, tag = "32")]
	# pub victory_points_earned: u32,

	# #[prost(uint32, tag = "33")]
	# pub victory_points_seized: u32,

	# /// Player's account ID.
	# #[prost(uint32, tag = "101")]
	# pub account_id: u32,

	# /// Player's tank ID as per Wargaming.net API.
	# #[prost(uint32, tag = "103")]
	# pub tank_id: u32,

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
	
	# /// Battle timestamp.
	# #[prost(int64, tag = "2")]
	# pub timestamp_secs: i64,
	battle_start_timestamp : Annotated[int64, Field(2)]

	# #[prost(enumeration = "TeamNumber", optional, tag = "3")]
	# pub winner_team_number: Option<i32>,
	winner_team : Annotated[Optional[int], Field(3)] = None

	# Field 4: spawn(NO)
	# xxx : Annotated[uint, Field(4)] = uint(1)

	# Field 5: unknown
	# xxx : Annotated[uint, Field(4)] = uint(1)

	# /// Replay's author results.
	# #[prost(message, required, tag = "8")]
	# pub author: Author,
	protagonist: Annotated[Protagonist, Field(8)]

	# Field 9: room_type
	# This is also shown in 'meta.json' file's 'arenaBonusType' field
	room_type : Annotated[uint, Field(9)] = uint(0)

	# /// Author's free XP, including premium.
	# #[prost(uint32, tag = "137")]
	# pub free_xp: u32,
	free_xp : Annotated[uint, Field(137)] = uint(0)

	# /// Players in the battle.
	# #[prost(message, repeated, tag = "201")]
	# pub players: Vec<Player>,
	players : Annotated[list[Player], Field(201)] = list()

	# /// Individual player's results.
	# #[prost(message, repeated, tag = "301")]
	# pub player_results: Vec<PlayerResults>,
	players_results : Annotated[list[PlayerResults], Field(301)] = list()


	@root_validator(pre=False)
	def read_map_id(cls, values: dict[str, Any]) -> dict[str, Any]:
		# map_id (Field=1) has sometimes a flag 0x1 set
		# i.e. Field = map_id | (0x1 << 16 )
		map_id : int = int(values['map_id'])
		values['map_id'] 	  = map_id  & 0xffff  # First 2 bytes
		values['battle_mode'] = map_id >> 16      # second 2 bytes 
		return values