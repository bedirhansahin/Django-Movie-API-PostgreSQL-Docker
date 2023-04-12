select * from core_user;
truncate table core_user CASCADE;

INSERT INTO core_user(password, is_superuser, username, first_name, last_name, email,
                      is_staff, is_active, birth_date, gender, date_joined)
VALUES('pbkdf2_sha256$600000$OXxSi6imAMLJvrKLZ8wjoY$k28zjj0dn1MC0uUR67kYxbzA0IS0qWBiziWKE0Mvffg=',
       true, 'admin', 'admin', 'admin', 'admin@admin.com',
       true, true, '1992-11-01', 'M', CURRENT_TIMESTAMP);


insert into core_genre (name, slug)
values ('Action', 'action');
insert into core_genre (name, slug)
values ('Comedy Western', 'comedy-western');
insert into core_genre (name, slug)
values ('Sci-Fi', 'sci-fi');
insert into core_genre (name, slug)
values ('Comedy', 'comedy');
insert into core_genre (name, slug)
values ('Horror', 'horror');
insert into core_genre (name, slug)
values ('Crime', 'crime');
insert into core_genre (name, slug)
values ('Musicals', 'musical');
insert into core_genre (name, slug)
values ('Romantic', 'romantic');


insert into core_director(name, slug)
values('Alfred Hitchcock', 'alfred-hitchcock');
insert into core_director(name, slug)
values('Francis Ford Coppola', 'francis-ford-coppola');
insert into core_director(name, slug)
values('Frank Capra', 'frank-capra');
insert into core_director(name, slug)
values('Stanley Kubrick', 'stanley-kubrick');
insert into core_director(name, slug)
values('Cristopher Nolan', 'cristopher-nolan');
insert into core_director(name, slug)
values('Nuri Bilge Ceylan', 'nuri-bilge-ceylan');



CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

select * from core_movie;
insert into core_movie (movie_id, movie_name, country, production_year, imdb, director_id, duration, story_line)
values (public.uuid_generate_v4(), 'Ahlat Ağacı', 'TR', 2018, 8.5, 6, 185, 'Sinai returns from his study in the city of Canakkale to his parents'' home in the small rural town of Can. He hopes to publish a book of essays and short stories. But his teacher father Idris is an addictive gambler, so much so that his mother and sister have become reluctantly accustomed to making do without food or electricity.');
insert into core_movie (movie_id, movie_name, country, production_year, imdb, director_id, duration, story_line)
values (public.uuid_generate_v4(), 'The Dark Knight', 'US', 2008, 8.9, 5, 152, 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.');
insert into core_movie (movie_id, movie_name, country, production_year, imdb, director_id, duration, story_line)
values (public.uuid_generate_v4(), 'The Shining', 'US', 1980, 8.4, 4, 146, 'A family heads to an isolated hotel for the winter where a sinister presence influences the father into violence, while his psychic son sees horrific forebodings from both past and future.');
insert into core_movie (movie_id, movie_name, country, production_year, imdb, director_id, duration, story_line)
values (public.uuid_generate_v4(), 'It''s a Wonderful Life' , 'GB', 1946, 8.6, 3, 130, 'An angel is sent from Heaven to help a desperately frustrated businessman by showing him what life would have been like if he had never existed.');
insert into core_movie (movie_id, movie_name, country, production_year, imdb, director_id, duration, story_line)
values (public.uuid_generate_v4(), 'The Birds', 'US', 1963, 7.6, 1, 119, 'A wealthy San Francisco socialite pursues a potential boyfriend to a small Northern California town that slowly takes a turn for the bizarre when birds of all kinds suddenly begin to attack people.');

