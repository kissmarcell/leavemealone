import { Provider } from "@/constants/Values"

export type ProjectListRequest = ProjectType[]

export type IssueType = {
    id: number,
    name: string,
    tags: string[],
    url: string,
}

export type ProjectType = {
    issues: IssueType[],
    name: string,
    provider: Provider,
}