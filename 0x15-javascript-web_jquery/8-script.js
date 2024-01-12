$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
sh: 1: q: not found
