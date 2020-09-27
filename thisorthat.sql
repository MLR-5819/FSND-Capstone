--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4
-- Dumped by pg_dump version 12.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
\.


--
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.category (id, type) FROM stdin;
1	Food
2	Cats
3	Dogs
4	Tattoos
5	Places
6	Cars
\.


--
-- Data for Name: entry; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.entry (id, name, category, entry_url, votes, date) FROM stdin;
1	Pizza	1	https://www.biggerbolderbaking.com/wp-content/uploads/2019/07/15-Minute-Pizza-WS-Thumbnail.png	1	2020-09-13
2	Grumpy Cat	2	https://media.wired.com/photos/5cdefb92b86e041493d389df/master/pass/Culture-Grumpy-Cat-487386121.jpg	2	2020-09-13
6	Grand Canal, Venice	5	https://cdn.getyourguide.com/niwziy2l9cvz/5jvou2r9leAUCaQO0mUcMk/e30f6e1c750f91ffeab8a7dc3af85d27/venice-grand-canal-1500-850__2_.jpg	0	2020-09-18
7	Geometric Rose	4	https://tattooabyss.com/wp-content/uploads/2019/05/geometric-rose-3cover-up-abby-tattoo-abyss.jpg	0	2020-09-18
5	Classic Corvette	6	https://images-na.ssl-images-amazon.com/images/I/81NMaWb1MuL._AC_SL1200_.jpg	0	2020-09-18
11	Shelby Mustang	6	https://i.pinimg.com/originals/7b/a8/7e/7ba87e2dbc00f4d081cc712b20a23e9e.jpg	0	2020-09-19
12	Fluffy	2	https://images.theconversation.com/files/312307/original/file-20200128-81416-1bjupq6.jpg	0	2020-09-19
13	Spot the Boxer	3	https://www.pets4homes.co.uk/images/articles/5285/large/white-boxer-dogs-what-you-need-to-know-about-the-white-boxer-dog-5c61a0f4568bb.jpeg	0	2020-09-19
14	London	5	https://www.history.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTYyNDg1MjE3MTI1Mjc5Mzk4/topic-london-gettyimages-760251843-promo.jpg	0	2020-09-19
15	Full Chest Tat	4	https://cdn.improb.com/wp-content/uploads/2017/10/mens-full-chest-tattoos-top-90-best-chest-tattoos-for-men-manly-designs-and-ideas-with.jpg	0	2020-09-19
8	Doug the Pug	3	https://i.pinimg.com/originals/d4/fb/52/d4fb52e5c6a4c5238d8d2169b8fe8293.jpg	0	2020-09-19
16	Juicy Burger	1	https://www.tasteofhome.com/wp-content/uploads/2018/01/Scrum-Delicious-Burgers_EXPS_CHMZ19_824_B10_30_2b-1.jpg	0	2020-09-24
\.


--
-- Name: category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.category_id_seq', 6, true);


--
-- Name: entry_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.entry_id_seq', 16, true);


--
-- PostgreSQL database dump complete
--

