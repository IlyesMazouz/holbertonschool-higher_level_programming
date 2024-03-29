-- This SQL script lists all shows contained in the 'hbtn_0d_tvshows' database without a genre linked
-- Each record displays: tv_shows.title - tv_show_genres.genre_id
-- The results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- The script uses a LEFT JOIN operation and filters out records where tv_show_genres.show_id is NULL

-- Listing shows without a linked genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
