#####################
# DEVELOPMENT IMAGE #
#####################
FROM node:14.17-buster as development

WORKDIR /usr/src/app
ENV CI=true
COPY package.json yarn.lock ./
RUN yarn install

COPY . .

EXPOSE 3000
CMD ["yarn", "start"]

####################
# PRODUCTION BUILD #
####################
FROM development as build

COPY .env ./
RUN yarn build

##########################
# FINAL PRODUCTION IMAGE #
##########################
FROM nginx:1.21 as production

COPY .docker/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf

WORKDIR /usr/share/nginx
RUN rm -rf html;
COPY --from=build /var/www/build ./html
COPY .env ./html

EXPOSE 3000
ENTRYPOINT ["nginx", "-g", "daemon off"]
