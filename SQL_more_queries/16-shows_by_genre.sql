-- This SQL script lists all shows and all genres linked to each show in the 'hbtn_0d_tvshows' database
-- It selects show titles and genre names from the 'tv_shows', 'tv_genres', and 'tv_show_genres' tables using LEFT JOINs
-- Results are sorted in ascending order by show title and genre name

-- Listing all shows and genres linked to each show
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
