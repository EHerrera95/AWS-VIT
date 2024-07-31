chmod g+x AWS-VIT && chmod g+x AWS-VIT/InspectTool && chmod g+x AWS-VIT/InspectTool/static

cd /etc/nginx/sites-enabled
sudo rm /etc/nginx/sites-enabled/InspectTool

server {
    listen 80;
    server_name 'visual-inspection-tool.dg-testlab.com';

    #location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ubuntu/AWS-VIT/InspectTool;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
~                           


sudo vi /etc/nginx/sites-enabled/default
sudo nginx -t && sudo systemctl restart nginx


sudo vi AWS-VIT/InspectTool/settings.py
sudo systemctl restart gunicorn

sudo chown -R ubuntu:ubuntu /home/ubuntu/AWS-VIT/media/media
sudo chmod -R u+rwX /home/ubuntu/AWS-VIT/media/media