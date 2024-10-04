import { api } from "@/api/client";
import Project from "@/components/project/Project";
import { ProjectListRequest } from "@/types/project";
import { useEffect, useState } from "react";

const Projects = () => {

  const fetchProjects = () => {
    api
      .fetchData<ProjectListRequest>("/projects")
      .then((projects) => setProjects(projects));
  }

  useEffect(() => {
    fetchProjects();
    const interval = setInterval(fetchProjects, 300000);
    return () => clearInterval(interval);
  }, []);

  const [projects, setProjects] = useState<ProjectListRequest>([]);

  return (
    <div style={styles.container}>
      {projects
        .filter((project) => project.issues.length != 0)
        .map((project) => (
          <Project project={project} />
        ))}
    </div>
  );
};

const styles = {
  container: {
    display: "flex",
    flexDirection: "column",
    color: "#fff",
    marginTop: "20px",
  },
} as const;

export default Projects;
