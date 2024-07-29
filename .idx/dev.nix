{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-23.11"; # or "unstable"

  # Use https://search.nixos.org/packages to find packages
  packages = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.python311Packages.virtualenv
  ];

  # Sets environment variables in the workspace
  env = {
    # Configure Python path
    PYTHONPATH = "${pkgs.python311Packages.python}/lib/python3.11/site-packages";
  };

  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [
      "ms-python.debugpy"
      "ms-python.python"
    ];

    # Enable previews
    previews = {
      enable = true;
      previews = {
        # web = {
        #   # Example: run "npm run dev" with PORT set to IDX's defined port for previews,
        #   # and show it in IDX's web preview panel
        #   command = ["npm" "run" "dev"];
        #   manager = "web";
        #   env = {
        #     # Environment variables to set for your server
        #     PORT = "$PORT";
        #   };
        # };
      };
    };

    # Workspace lifecycle hooks
    workspace = {
      # Runs when a workspace is first created
      onCreate = {
        # Create and activate a virtual environment
        virtualenv = "python -m venv venv";
        pip-install = "venv/bin/pip install moviepy pytube";
      };
      # Runs when the workspace is (re)started
      onStart = {
        # Ensure virtualenv is activated before running scripts
        activate-venv = "source venv/bin/activate";
      };
    };
  };
}
