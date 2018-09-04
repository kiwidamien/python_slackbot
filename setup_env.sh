#!/bin/sh
heroku config:set $(<.env)
