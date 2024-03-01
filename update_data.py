from datetime import datetime
from athetes_unlimited_py.aux_softball import (
    get_aux_softball_season_pbp,
    get_aux_softball_season_player_box,
    get_aux_softball_season_team_box,
    get_aux_softball_season_player_stats,
    get_aux_softball_season_team_stats,
)
from athetes_unlimited_py.softball import (
    get_au_softball_season_pbp,
    get_au_softball_season_player_box,
    get_au_softball_season_player_stats,
    get_au_softball_season_team_box,
    get_au_softball_season_team_stats,
)
from athetes_unlimited_py.basketball import (
    get_au_basketball_season_pbp,
    get_au_basketball_season_player_box,
    get_au_basketball_season_team_box,
    get_au_basketball_season_player_stats,
    get_au_basketball_season_team_stats,
)
from athetes_unlimited_py.lacrosse import (
    get_au_lacrosse_season_pbp,
    get_au_lacrosse_season_player_box,
    get_au_lacrosse_season_team_box,
    get_au_lacrosse_season_player_stats,
    get_au_lacrosse_season_team_stats,
)
from athetes_unlimited_py.volleyball import (
    get_au_volleyball_season_pbp,
    get_au_volleyball_season_player_box,
    get_au_volleyball_season_player_stats,
    get_au_volleyball_season_team_box,
    get_au_volleyball_season_team_stats,
)


def update_aux_softball(season: int):
    print(f"\n\nDownloading AUX Softball play-by-play data for {season}.\n")
    pbp_df = get_aux_softball_season_pbp(season)

    if len(pbp_df) > 0:
        pbp_df.to_csv(f"aux_softball/pbp/{season}_aux_softball_pbp.csv", index=False)

    del pbp_df

    print(f"\n\nDownloading AUX Softball player game stats for {season}.\n")

    stats_df = get_aux_softball_season_player_box(season)

    if len(stats_df) > 0:
        stats_df.to_csv(
            f"aux_softball/player_stats/game_stats/{season}_aux_softball_player_game_stats.csv",
            index=False,
        )

    del stats_df

    print(f"\n\nDownloading AUX Softball player season stats for {season}.\n")

    stats_df = get_aux_softball_season_player_stats(season)

    if len(stats_df) > 0:
        stats_df.to_csv(
            f"aux_softball/player_stats/season_stats/{season}_aux_softball_player_season_stats.csv",
            index=False,
        )

    del stats_df

    print(f"\n\nDownloading AUX Softball team game stats for {season}.\n")

    stats_df = get_aux_softball_season_team_box(season)

    if len(stats_df) > 0:
        stats_df.to_csv(
            f"aux_softball/team_stats/game_stats/{season}_aux_softball_team_game_stats.csv",
            index=False,
        )

    del stats_df

    print(f"\n\nDownloading AUX Softball team season stats for {season}.\n")

    stats_df = get_aux_softball_season_team_stats(season)

    if len(stats_df) > 0:
        stats_df.to_csv(
            f"aux_softball/team_stats/season_stats/{season}_aux_softball_team_season_stats.csv",
            index=False,
        )

    del stats_df


def update_au_softball(season: int):
    print(f"\n\nDownloading AU Softball play-by-play data for {season}.\n")
    pbp_df = get_au_softball_season_pbp(season)

    if len(pbp_df) > 0:
        pbp_df.to_csv(f"softball/pbp/{season}_softball_pbp.csv", index=False)

    del pbp_df

    print(f"\n\nDownloading AU Softball player game stats for {season}.\n")

    stats_df = get_au_softball_season_player_box(season)

    if len(stats_df) > 0:
        stats_df.to_csv(
            f"softball/player_stats/game_stats/{season}_softball_player_game_stats.csv",
            index=False,
        )

    del stats_df

    print(f"\n\nDownloading AU Softball player season stats for {season}.\n")

    stats_df = get_au_softball_season_player_stats(season)

    if len(stats_df) > 0:
        stats_df.to_csv(
            f"softball/player_stats/season_stats/{season}_softball_player_season_stats.csv",
            index=False,
        )

    del stats_df

    print(f"\n\nDownloading AU Softball team game stats for {season}.\n")

    stats_df = get_au_softball_season_team_box(season)

    if len(stats_df) > 0:
        stats_df.to_csv(
            f"softball/team_stats/game_stats/{season}_softball_team_game_stats.csv",
            index=False,
        )

    del stats_df

    print(f"\n\nDownloading AU Softball team season stats for {season}.\n")

    stats_df = get_au_softball_season_team_stats(season)

    if len(stats_df) > 0:
        stats_df.to_csv(
            f"softball/team_stats/season_stats/{season}_softball_team_season_stats.csv",
            index=False,
        )

    del stats_df


def update_au_basketball(season: int):
    print(f"\n\nDownloading AU basketball play-by-play data for {season}.\n")
    pbp_df = get_au_basketball_season_pbp(season)

    if len(pbp_df) > 0:
        pbp_df.to_csv(f"basketball/pbp/{season}_basketball_pbp.csv", index=False)

    del pbp_df

    print(f"\n\nDownloading AU basketball player game stats for {season}.\n")

    stats_df = get_au_basketball_season_player_box(season)

    if len(stats_df) > 0:
        stats_df.to_csv(
            f"basketball/player_stats/game_stats/{season}_basketball_player_game_stats.csv",
            index=False,
        )

    del stats_df

    print(f"\n\nDownloading AU basketball player season stats for {season}.\n")

    stats_df = get_au_basketball_season_player_stats(season)

    if len(stats_df) > 0:
        stats_df.to_csv(
            f"basketball/player_stats/season_stats/{season}_basketball_player_season_stats.csv",
            index=False,
        )

    del stats_df

    print(f"\n\nDownloading AU basketball team game stats for {season}.\n")

    stats_df = get_au_basketball_season_team_box(season)

    if len(stats_df) > 0:
        stats_df.to_csv(
            f"basketball/team_stats/game_stats/{season}_basketball_team_game_stats.csv",
            index=False,
        )

    del stats_df

    print(f"\n\nDownloading AU basketball team season stats for {season}.\n")

    stats_df = get_au_basketball_season_team_stats(season)

    if len(stats_df) > 0:
        stats_df.to_csv(
            f"basketball/team_stats/season_stats/{season}_basketball_team_season_stats.csv",
            index=False,
        )

    del stats_df


def update_au_lacrosse(season: int):
    print(f"\n\nDownloading AU lacrosse play-by-play data for {season}.\n")
    pbp_df = get_au_lacrosse_season_pbp(season)

    if len(pbp_df) > 0:
        pbp_df.to_csv(f"lacrosse/pbp/{season}_lacrosse_pbp.csv", index=False)

    del pbp_df

    print(f"\n\nDownloading AU lacrosse player game stats for {season}.\n")

    stats_df = get_au_lacrosse_season_player_box(season)

    if len(stats_df) > 0:
        stats_df.to_csv(
            f"lacrosse/player_stats/game_stats/{season}_lacrosse_player_game_stats.csv",
            index=False,
        )

    del stats_df

    print(f"\n\nDownloading AU lacrosse player season stats for {season}.\n")

    stats_df = get_au_lacrosse_season_player_stats(season)

    if len(stats_df) > 0:
        stats_df.to_csv(
            f"lacrosse/player_stats/season_stats/{season}_lacrosse_player_season_stats.csv",
            index=False,
        )

    del stats_df

    print(f"\n\nDownloading AU lacrosse team game stats for {season}.\n")

    stats_df = get_au_lacrosse_season_team_box(season)

    if len(stats_df) > 0:
        stats_df.to_csv(
            f"lacrosse/team_stats/game_stats/{season}_lacrosse_team_game_stats.csv",
            index=False,
        )

    del stats_df

    print(f"\n\nDownloading AU lacrosse team season stats for {season}.\n")

    stats_df = get_au_lacrosse_season_team_stats(season)

    if len(stats_df) > 0:
        stats_df.to_csv(
            f"lacrosse/team_stats/season_stats/{season}_lacrosse_team_season_stats.csv",
            index=False,
        )

    del stats_df


def update_au_volleyball(season: int):
    print(f"\n\nDownloading AU volleyball play-by-play data for {season}.\n")
    pbp_df = get_au_volleyball_season_pbp(season)

    if len(pbp_df) > 0:
        pbp_df.to_csv(f"volleyball/pbp/{season}_volleyball_pbp.csv", index=False)

    del pbp_df

    print(f"\n\nDownloading AU volleyball player game stats for {season}.\n")

    stats_df = get_au_volleyball_season_player_box(season)

    if len(stats_df) > 0:
        stats_df.to_csv(
            f"volleyball/player_stats/game_stats/{season}_volleyball_player_game_stats.csv",
            index=False,
        )

    del stats_df

    print(f"\n\nDownloading AU volleyball player season stats for {season}.\n")

    stats_df = get_au_volleyball_season_player_stats(season)

    if len(stats_df) > 0:
        stats_df.to_csv(
            f"volleyball/player_stats/season_stats/{season}_volleyball_player_season_stats.csv",
            index=False,
        )

    del stats_df

    print(f"\n\nDownloading AU volleyball team game stats for {season}.\n")

    stats_df = get_au_volleyball_season_team_box(season)

    if len(stats_df) > 0:
        stats_df.to_csv(
            f"volleyball/team_stats/game_stats/{season}_volleyball_team_game_stats.csv",
            index=False,
        )

    del stats_df

    print(f"\n\nDownloading AU volleyball team season stats for {season}.\n")

    stats_df = get_au_volleyball_season_team_stats(season)

    if len(stats_df) > 0:
        stats_df.to_csv(
            f"volleyball/team_stats/season_stats/{season}_volleyball_team_season_stats.csv",
            index=False,
        )

    del stats_df


if __name__ == "__main__":
    #year = 2023
    now = datetime.now()
    # update_aux_softball(now.year)
    # update_au_softball(now.year)
    update_au_basketball(now.year)
    # update_au_lacrosse(now.year)
    # update_au_volleyball(now.year)

    # for i in range(2021, 2023):
    #     update_au_volleyball(i)
