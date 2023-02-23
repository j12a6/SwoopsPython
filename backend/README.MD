# Swoops statistics package

This is a Swoops statistics package.

See
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to use markdown.

### Swoops API
___

#### Available
- https://api.playswoops.com/api/game/723/
(723 is the first accessible game)
- https://api.playswoops.com/api/game/player/leaderboard
- https://api.playswoops.com/api/game/team/88/
- https://api.playswoops.com/api/game/ (open games at the moment)

#### Needs auth:
- https://api.playswoops.com/api/game/team/

### Useful commands
___
- ```grep -rnw '../databases/swoops/api/games' -e 'Not found' | wc -l```
- ```grep -rnw '../databases/swoops/api/games' -e 'Bad Gateway' | wc -l```


- ```npx tailwindcss -i ./front/static/src/input.css -o ./front/static/dist/css/output.css --watch```
- ```flask --app front --debug run```

### Tools
___

- https://www.flaticon.com/free-icon/eye_159604?related_id=159604
- https://icolorpalette.com/color?q=3364b8
