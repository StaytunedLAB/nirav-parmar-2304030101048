import { Octokit } from "@octokit/core";

const octokit = new Octokit({
    auth: "CLASSIC TOKAN"
});

async function createIssue () {
    try {
        await octokit.request('POST /repos/StaytunedLAB/nirav-parmar-2304030101048/issues', {
            owner: 'StaytunedLAB',
            repo: 'nirav-parmar-2304030101048',
            title: 'issue created using javascript code',
            body: "issue created using javascript code using rest api key token.",
            headers: {
                'X-GitHub-Api-Version': '2022-11-28'
            }
        });
        console.log("issue created");
    } catch (error) {
        console.error("Error creating issue:", error);
    }
}
createIssue();
