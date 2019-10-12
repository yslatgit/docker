FROM nginx:1.14-alpine
#RUN mkdir -p /e
ADD entrypoint.sh /bin/
ENV NGX_ROOT /usr/www/
COPY index.html ${NGX_ROOT}
CMD ["/usr/sbin/nginx","-g","daemon off;"]
HEALTHCHECK --interval=3s --timeout=2s --retries=2 CMD wget --spider localhost
ENTRYPOINT ["entrypoint.sh"]
