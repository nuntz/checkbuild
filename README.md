# checkbuild

This image compares the timestamps of the *latest* builds for two Docker Hub images (assuming one of them is the the image the other one is based on -- aka base image), and executes an HTTP post to trigger a new build if the base image is more recent.

I created this image because the Docker Hub repository links build option only works for non-official images.

## Usage

```bash
docker run --env-file=.env checkbuild
```

This can easily be configured to run as cron job on the host.

## Environment Variables

Define these in your `.env` file:

* `BASE_USERNAME`: username of the upstream image repository
* `BASE_REPOSITORY`: name of the upstream image repository
* `MY_USERNAME`: your username
* `MY_REPOSITORY`: your repository
* `BUILD_TRIGGER_URL`: trigger build URL
* `SLACK_WEBHOOK`: Slack webhook for notifications
